function updateCharts(tasks) {
    const labelData = processLabelData(tasks);
    const completedTasksData = processCompletedTasksData(tasks);
    const tasksByStatusData = processTasksByStatusData(tasks);

    createLabelChart(labelData);
    createCompletedTasksChart(completedTasksData);
    createTasksByStatusChart(tasksByStatusData);
}

function createLabelChart(data) {
    console.log('Creando gráfico de etiquetas...');
    const ctx = document.getElementById('labelChart').getContext('2d');
    if (!ctx) {
        console.error('No se pudo encontrar el elemento canvas para el gráfico de etiquetas');
        return;
    }

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

function createTasksByStatusChart(data) {
    console.log('Creando gráfico de tareas por estado...');
    const ctx = document.getElementById('tasksByStatusChart').getContext('2d');
    if (!ctx) {
        console.error('No se pudo encontrar el elemento canvas para el gráfico de tareas por estado');
        return;
    }

    if (tasksByStatusChart) {
        tasksByStatusChart.destroy();
    }

    const statuses = Object.keys(data);
    const projects = [...new Set(Object.values(data).flatMap(Object.keys))];
    const datasets = projects.map(project => ({
        label: project,
        data: statuses.map(status => data[status][project] || 0),
        backgroundColor: getProjectColor(project)
    }));

    tasksByStatusChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: statuses,
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
                    text: 'Total de Tareas por Estado y Proyecto'
                }
            }
        }
    });
}