const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute('data-pk')
    const examName = modalBtn.getAttribute('data-exam')
    const subject = modalBtn.getAttribute('data-subject')
    const teacher = modalBtn.getAttribute('data-teacher')
    const getThree = modalBtn.getAttribute('data-three')
    const getFour = modalBtn.getAttribute('data-four')
    const getFive = modalBtn.getAttribute('data-five')
    const getSix = modalBtn.getAttribute('data-six')

    modalBody.innerHTML = `
    <div class="text-center h5 mb-4">Сигурен ли си че искаш да започнеш "${examName}"?</div>
    <div class="text-muted">
        <ul>
            <li><b>Предмет: ${subject}</b></li>
            <li>Учител: ${teacher}</li>
            <li>Процент верни отговори за 3.00: ${getThree}%</li>
            <li>Процент верни отговори за 3.50: ${getFour}%</li>
            <li>Процент верни отговори за 4.50: ${getFive}%</li>
            <li>Процент верни отговори за 5.50: ${getSix}%</li>
        </ul>    
    </div>`

    startBtn.addEventListener('click', () => {
        window.location.href = url + pk
    })
}))