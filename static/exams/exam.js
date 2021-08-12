const url = window.location.href
const examBox = document.getElementById('exam-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')

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
            const results = response.results

            examForm.classList.add('not-visible')

            scoreBox.classList.add('bg-info')

            scoreBox.classList.add(...['container', 'p-3', 'text-light', 'h3'])
            scoreBox.innerHTML += `Твоят резултат е ${response.score}%\nОценка: ${response.grade}`
            console.log(response.grade)
            results.forEach(r => {

                const resultDiv = document.createElement('div')
                resultDiv.style.borderRadius = '5px'
                resultDiv.style.paddingTop = '5px'

                for (const [question, answer] of Object.entries(r)) {
                    resultDiv.innerHTML += question
                    const divClasses = ['container', 'p-3', 'text-light', 'h3']
                    resultDiv.classList.add(...divClasses)

                    if (answer === 'Не е отговорен') {
                        resultDiv.innerHTML += `<br>Не е отговорен`
                        resultDiv.classList.add('bg-danger')
                    } else {
                        const answered = answer['selected']
                        const correctAnswer = answer['correct']
                        if (answered === correctAnswer) {
                            resultDiv.classList.add('bg-success')
                            resultDiv.innerHTML += `<br>Правилен отговор: ${answered}`
                        } else {
                            resultDiv.classList.add('bg-danger')
                            resultDiv.innerHTML += `<br>Избран отговор: ${answered}<br>Верен отговор: ${correctAnswer}`
                        }
                    }
                }
                resultBox.append(resultDiv)
            })
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