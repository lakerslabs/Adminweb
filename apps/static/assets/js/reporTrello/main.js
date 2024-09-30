// Variables globales
let labelChart;
let completedTasksChart;
let tasksByStatusChart;
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

// Cargar los datos del archivo JSON que se encuentra en la carpeta media de proyecto Django
// fetch('/media/reporte_completo_trello_con_acciones.json')
//     .then(response => response.json())
//     .then(data => {
//         console.log('Datos JSON cargados correctamente:', data);
//         processData(data);
//     })
//     .catch(error => {
//         console.error('Error al cargar o procesar los datos:', error);
//         document.body.innerHTML += `<p>Error al cargar los datos: ${error.message}</p>`;
//     });
    

// Cargar los datos del archivo JSON
fetch('/media/Trello.json')
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
        updateTasksTable(globalTasks);
        setupFilters();
    } catch (error) {
        console.error('Error en el procesamiento de datos:', error);
        document.body.innerHTML += `<p>Error en el procesamiento de datos: ${error.message}</p>`;
    }
};

function exportReport() {
  window.print();
}

// Evento para el botón de exportar (aún no implementado)
// document.getElementById('exportButton').addEventListener('click', () => {
//     console.log('Función de exportación llamada');
//     alert('Funcionalidad de exportación no implementada');
// });

