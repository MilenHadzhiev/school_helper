const url = window.location.href

const examBox = document.getElementById('exam-box')
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        let data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                examBox.innerHTML += `
                <hr>
                <div class="mb-2">
                    <b>${question}</b>
                </div>
                `
                answers.forEach(answer => {
                    examBox.innerHTML += `
                    <div>
                        <input type="radio" 
                               class="answer" 
                               id="${question}-${answer}" 
                               name="${question}" 
                               value="${answer}">
                        <label for="${question}">${answer}</label>
                    </div>`
                })
            }
        });
    },
    error: function (error) {
        console.log(error)
    }
})

const examForm = document.getElementById('exam-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('answer')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            const redirect_url = response['redirect_url']
            console.log(redirect_url)
            window.location.replace(redirect_url)
        },
        error: function (error) {
            console.log(error)
        }
    })
}

examForm.addEventListener('submit', event => {
    event.preventDefault()
    sendData()
})
