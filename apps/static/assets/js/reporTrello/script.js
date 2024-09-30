// Variables globales para mantener referencia a los gráficos y tareas
let labelChart;
let completedTasksChart;
let globalTasks;

// Colores consistentes para los proyectos
const projectColors = {
    'Proyecto A': '#FF6384',
    'Proyecto B': '#36A2EB',
    'Proyecto C': '#FFCE56',
    'Proyecto D': '#4BC0C0',
    'Proyecto E': '#9966FF',
    'Proyecto F': '#FF9F40'
};

// Función para obtener color o generar uno nuevo si no existe
function getProjectColor(project) {
    if (!projectColors[project]) {
        projectColors[project] = `#${Math.floor(Math.random()*16777215).toString(16)}`;
    }
    return projectColors[project];
}

// Cargar los datos del archivo JSON
fetch('reporte_completo_trello_con_acciones.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Datos JSON cargados correctamente:', data);
        processData(data);
    })
    .catch(error => {
        console.error('Error al cargar o procesar los datos:', error);
        document.body.innerHTML += `<p>Error al cargar los datos: ${error.message}</p>`;
    });

function processData(data) {
    try {
        console.log('Procesando datos...');
        globalTasks = extractTasks(data);
        console.log('Tareas extraídas:', globalTasks);

        updateCharts(globalTasks);
        setupFilters();
    } catch (error) {
        console.error('Error en el procesamiento de datos:', error);
        document.body.innerHTML += `<p>Error en el procesamiento de datos: ${error.message}</p>`;
    }
}

function extractTasks(data) {
    console.log('Extrayendo tareas...');
    if (!data.Listas || !Array.isArray(data.Listas)) {
        throw new Error('Estructura de datos inválida: "Listas" no encontrado o no es un array');
    }
    return data.Listas.flatMap(lista => {
        if (!lista.Tarjetas || !Array.isArray(lista.Tarjetas)) {
            console.warn(`Lista "${lista.Lista.name}" no tiene Tarjetas o no es un array`);
            return [];
        }
        return lista.Tarjetas.map(tarjeta => ({
            name: tarjeta.Tarjeta.name,
            labels: tarjeta.Tarjeta.labels ? tarjeta.Tarjeta.labels.map(label => label.name) : [],
            list: lista.Lista.name,
            dateLastActivity: new Date(tarjeta.Tarjeta.dateLastActivity)
        }));
    });
}

function updateCharts(tasks) {
    const labelData = processLabelData(tasks);
    const completedTasksData = processCompletedTasksData(tasks);

    createLabelChart(labelData);
    createCompletedTasksChart(completedTasksData);
}

function processLabelData(tasks) {
    console.log('Procesando datos de etiquetas...');
    const labelCounts = {};
    tasks.forEach(task => {
        task.labels.forEach(label => {
            labelCounts[label] = (labelCounts[label] || 0) + 1;
        });
    });
    const total = Object.values(labelCounts).reduce((sum, count) => sum + count, 0);
    return Object.fromEntries(
        Object.entries(labelCounts).map(([label, count]) => [label, (count / total) * 100])
    );
}

function processCompletedTasksData(tasks) {
    console.log('Procesando datos de tareas completadas...');
    const completedTasks = tasks.filter(task => task.list === 'Finalizadas');
    const tasksByDay = {
        'Lunes': {}, 'Martes': {}, 'Miércoles': {}, 'Jueves': {}, 'Viernes': {}, 'Sábado': {}, 'Domingo': {}
    };
    const daysOfWeek = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];

    completedTasks.forEach(task => {
        const day = daysOfWeek[task.dateLastActivity.getDay()];
        task.labels.forEach(label => {
            tasksByDay[day][label] = (tasksByDay[day][label] || 0) + 1;
        });
    });

    return tasksByDay;
}

function createLabelChart(data) {
    console.log('Creando gráfico de etiquetas...');
    const ctx = document.getElementById('labelChart').getContext('2d');
    if (!ctx) {
        console.error('No se pudo encontrar el elemento canvas para el gráfico de etiquetas');
        return;
    }

    // Destruir el gráfico existente si hay uno
    if (labelChart) {
        labelChart.destroy();
    }

    labelChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(data),
            datasets: [{
                data: Object.values(data),
                backgroundColor: Object.keys(data).map(getProjectColor)
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Porcentaje de Tareas por Proyecto'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const percentage = value.toFixed(2);
                            return `${label}: ${percentage}%`;
                        }
                    }
                }
            }
        }
    });
}

function createCompletedTasksChart(data) {
    console.log('Creando gráfico de tareas completadas...');
    const ctx = document.getElementById('completedTasksChart').getContext('2d');
    if (!ctx) {
        console.error('No se pudo encontrar el elemento canvas para el gráfico de tareas completadas');
        return;
    }

    // Destruir el gráfico existente si hay uno
    if (completedTasksChart) {
        completedTasksChart.destroy();
    }

    const orderedDays = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
    const labels = orderedDays;
    const projects = [...new Set(Object.values(data).flatMap(Object.keys))];
    const datasets = projects.map(project => ({
        label: project,
        data: labels.map(day => data[day][project] || 0),
        backgroundColor: getProjectColor(project)
    }));

    completedTasksChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            scales: {
                x: { stacked: true },
                y: { stacked: true }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Tareas Finalizadas por Día'
                }
            }
        }
    });
}

function setupFilters() {
    setupLabelFilter();
    setupProjectFilter();
    setupDateFilter();
}

function setupLabelFilter() {
    const labelFilter = document.getElementById('labelFilter');
    if (!labelFilter) {
        console.error('No se pudo encontrar el elemento de filtro de etiquetas');
        return;
    }

    // Limpiar opciones existentes
    labelFilter.innerHTML = '<option value="all">Todas las etiquetas</option>';

    const labels = [...new Set(globalTasks.flatMap(task => task.labels))];
    labels.forEach(label => {
        const option = document.createElement('option');
        option.value = label;
        option.textContent = label;
        labelFilter.appendChild(option);
    });

    labelFilter.addEventListener('change', applyFilters);
}

function setupProjectFilter() {
    const projectFilter = document.getElementById('projectFilter');
    if (!projectFilter) {
        console.error('No se pudo encontrar el elemento de filtro de proyectos');
        return;
    }

    // Limpiar opciones existentes
    projectFilter.innerHTML = '<option value="all">Todos los proyectos</option>';

    const projects = [...new Set(globalTasks.flatMap(task => task.labels))];
    projects.forEach(project => {
        const option = document.createElement('option');
        option.value = project;
        option.textContent = project;
        projectFilter.appendChild(option);
    });

    projectFilter.addEventListener('change', applyFilters);
}

function setupDateFilter() {
    const dateFilter = document.getElementById('dateFilter');
    if (!dateFilter) {
        console.error('No se pudo encontrar el elemento de filtro de fecha');
        return;
    }

    // Limpiar opciones existentes
    dateFilter.innerHTML = '';

    const options = [
        { value: 'all', text: 'Todas las fechas' },
        { value: 'today', text: 'Hoy' },
        { value: 'yesterday', text: 'Ayer' },
        { value: 'thisWeek', text: 'Semana actual' },
        { value: 'lastWeek', text: 'Semana anterior' },
        { value: 'thisMonth', text: 'Mes actual' },
        { value: 'lastMonth', text: 'Mes anterior' }
    ];

    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option.value;
        optionElement.textContent = option.text;
        dateFilter.appendChild(optionElement);
    });

    dateFilter.addEventListener('change', applyFilters);
}

function applyFilters() {
    const labelFilter = document.getElementById('labelFilter').value;
    const projectFilter = document.getElementById('projectFilter').value;
    const dateFilter = document.getElementById('dateFilter').value;

    let filteredTasks = globalTasks;

    if (labelFilter !== 'all') {
        filteredTasks = filteredTasks.filter(task => task.labels.includes(labelFilter));
    }

    if (projectFilter !== 'all') {
        filteredTasks = filteredTasks.filter(task => task.labels.includes(projectFilter));
    }

    filteredTasks = filterTasksByDate(filteredTasks, dateFilter);

    updateCharts(filteredTasks);
}

function filterTasksByDate(tasks, filter) {
    const today = new Date();
    const yesterday = new Date(today);
    yesterday.setDate(yesterday.getDate() - 1);

    switch (filter) {
        case 'today':
            return tasks.filter(task => isSameDay(task.dateLastActivity, today));
        case 'yesterday':
            return tasks.filter(task => isSameDay(task.dateLastActivity, yesterday));
        case 'thisWeek':
            return tasks.filter(task => isThisWeek(task.dateLastActivity));
        case 'lastWeek':
            return tasks.filter(task => isLastWeek(task.dateLastActivity));
        case 'thisMonth':
            return tasks.filter(task => isThisMonth(task.dateLastActivity));
        case 'lastMonth':
            return tasks.filter(task => isLastMonth(task.dateLastActivity));
        default:
            return tasks;
    }
}

function isSameDay(d1, d2) {
    return d1.getFullYear() === d2.getFullYear() &&
           d1.getMonth() === d2.getMonth() &&
           d1.getDate() === d2.getDate();
}

function isThisWeek(date) {
    const today = new Date();
    const firstDayOfWeek = new Date(today.setDate(today.getDate() - today.getDay()));
    const lastDayOfWeek = new Date(firstDayOfWeek);
    lastDayOfWeek.setDate(lastDayOfWeek.getDate() + 6);
    return date >= firstDayOfWeek && date <= lastDayOfWeek;
}

function isLastWeek(date) {
    const today = new Date();
    const lastWeekStart = new Date(today.setDate(today.getDate() - today.getDay() - 7));
    const lastWeekEnd = new Date(lastWeekStart);
    lastWeekEnd.setDate(lastWeekEnd.getDate() + 6);
    return date >= lastWeekStart && date <= lastWeekEnd;
}

function isThisMonth(date) {
    const today = new Date();
    return date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear();
}

function isLastMonth(date) {
    const today = new Date();
    const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1);
    return date.getMonth() === lastMonth.getMonth() && date.getFullYear() === lastMonth.getFullYear();
}

document.getElementById('exportButton').addEventListener('click', exportReport);

function exportReport() {
    console.log('Función de exportación llamada');
    alert('Funcionalidad de exportación no implementada');
}

// Asegúrate de que el DOM está completamente cargado antes de intentar acceder a los elementos
document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM completamente cargado y analizado');
});