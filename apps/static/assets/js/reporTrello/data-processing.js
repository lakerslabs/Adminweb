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
            dateLastActivity: new Date(tarjeta.Tarjeta.dateLastActivity),
            timeInProgress: calculateTimeInProgress(tarjeta.Acciones)
        }));
    });
}

function calculateTimeInProgress(acciones) {
    if (!acciones || acciones.length === 0) return 'N/A';

    let startTime, endTime;

    for (let i = acciones.length - 1; i >= 0; i--) {
        const accion = acciones[i];
        if (accion.data.listAfter && accion.data.listAfter.name === 'En progreso') {
            startTime = new Date(accion.date);
        }
        if (accion.data.listAfter && accion.data.listAfter.name === 'Finalizadas') {
            endTime = new Date(accion.date);
            break;
        }
    }

    if (startTime && endTime) {
        const diffHours = (endTime - startTime) / (1000 * 60 * 60);
        return diffHours.toFixed(2) + ' horas';
    }

    return 'N/A';
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

function processTasksByStatusData(tasks) {
    console.log('Procesando datos de tareas por estado...');
    const tasksByStatus = {};
    tasks.forEach(task => {
        if (!tasksByStatus[task.list]) {
            tasksByStatus[task.list] = {};
        }
        task.labels.forEach(label => {
            tasksByStatus[task.list][label] = (tasksByStatus[task.list][label] || 0) + 1;
        });
    });
    return tasksByStatus;
}