function setupFilters() {
    setupProjectFilter();
    setupDateFilter();
}

function setupProjectFilter() {
    const projectFilter = document.getElementById('projectFilter');
    if (!projectFilter) {
        console.error('No se pudo encontrar el elemento de filtro de proyectos');
        return;
    }

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
    const projectFilter = document.getElementById('projectFilter').value;
    const dateFilter = document.getElementById('dateFilter').value;

    let filteredTasks = globalTasks;

    if (projectFilter !== 'all') {
        filteredTasks = filteredTasks.filter(task => task.labels.includes(projectFilter));
    }

    filteredTasks = filterTasksByDate(filteredTasks, dateFilter);

    updateCharts(filteredTasks);
    updateTasksTable(filteredTasks);
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