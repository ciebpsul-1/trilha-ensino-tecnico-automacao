const input = document.querySelector('#currency');
const registerBtn = document.querySelector('#register-btn');
const tableBody = document.querySelector('tbody');

input.addEventListener('blur', ({ target }) => {
    const value = target.value.replace(/\.(?=.*\.)/g, '');

    if (!value) return;

    target.value = new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(Number(value));
});

input.addEventListener('focus', ({ target }) => {
    target.value = '';
});

registerBtn.addEventListener('click', () => {
    const row = document.createElement('tr');

    document.querySelectorAll('input').forEach(({ value }) => {
        const td = document.createElement('td');
        td.className = 'd-flex text-center';
        td.textContent = value;
        row.append(td);
    });

    document.querySelectorAll('input').forEach(input => {
        input.value = '';
    });

    tableBody.append(row);
});