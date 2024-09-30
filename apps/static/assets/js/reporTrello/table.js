function updateTasksTable(tasks) {
    const tableBody = document.querySelector('#tasksTable tbody');
    tableBody.innerHTML = ''; // Limpiar tabla existente

    tasks.forEach(task => {
        const row = tableBody.insertRow();
        row.insertCell(0).textContent = task.name;
        row.insertCell(1).textContent = task.labels.join(', ');
        row.insertCell(2).textContent = task.list;
        row.insertCell(3).textContent = task.dateLastActivity.toLocaleString();
        row.insertCell(4).textContent = task.timeInProgress;
    });
}