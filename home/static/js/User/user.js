let contents = JSON.parse(document.getElementById('contents').textContent);
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;


document.getElementById('form-change-info').addEventListener('submit', function (e) {
    e.preventDefault();
    let message = document.getElementById('message');
    let change_btn = document.getElementById('change_inf');
    change_btn.setAttribute('disabled','disabled')
    change_btn.textContent = 'loading...'
    let form_data = new FormData(this)
    let same_data=0
    let counter = 0
    for (const [k,v] of form_data) {
        if (!['change_information', 'csrfmiddlewaretoken'].includes(k)){
            counter++
            console.log(k,v)
            if (v === contents[k]) {
                same_data++;
            }
            // console.log(k,":",v,',',contents[k])
        }
    }
    if (counter !== same_data) {
        let email_v = document.getElementById('email').value;
        form_data.append('email', email_v)
        // for (const k of form_data) {
        //     console.log(k)
        // }
        message.removeAttribute('hidden')
        message.textContent = ''
        console.log('count:',counter, same_data)
        // const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch('/user/',{
            method: 'post',
            body: form_data,
            headers: {
                    'X-CSRFToken': csrfToken
                }
        }).then(res => res.json())
            .then(d => {
                if (d.status === 200){
                    message.removeAttribute('hidden')
                    message.textContent = d.msg
                    let c =3
                    let interval = setInterval(()=>{
                        c--
                        message.textContent = '页面'+ c + 's 后刷新'
                    },1000);
                    setTimeout(()=>{
                        clearInterval(interval)
                        location.reload()
                    },2000)
                }
            })
    }else{
        message.removeAttribute('hidden')
        message.textContent = '数据没有变化'
        setTimeout(()=>{
            change_btn.removeAttribute('disabled')
            change_btn.textContent = 'submit'
            },1000)
    }
})

document.getElementById('input-picture').addEventListener('change',function (e){
    const file = this.files[0]
    if(file && file.type.startsWith('image/')){
        const reader = new FileReader()
        reader.onload = function (event){
            const preview = document.getElementById('preview-picture')
            preview.src = event.target.result
            document.getElementById('preview').style.display = 'block'
        }
        reader.readAsDataURL(file)
    }
})

document.getElementById('user-picture').addEventListener('submit',function (e) {
    e.preventDefault()
    let data_form = new FormData(this)
    for (const [k,v] of data_form) {
        console.log(k,':',v)
    }
    let pb = document.getElementById('picture-btn')
    pb.setAttribute('disabled','disabled')
    let elementById = document.getElementById('picture-p');

    if (document.getElementById('input-picture').files.length !== 0){
        fetch('/user/',{
            method: 'post',
            headers:{
                'X-CSRFToken': csrfToken,
            },
            body: data_form
        })
            .then(res =>res.json())
            .then(d=>{
                if(d.status === 200){
                    let t = 3
                    elementById.removeAttribute('hidden')
                    elementById.textContent = d.msg
                    pb.textContent = 'uploading ...'
                    const refresh = setInterval(()=>{
                        t--
                        elementById.textContent = d.msg + ' will '+ t+'s refresh'
                    },1000)
                    setTimeout(() => {
                        clearInterval(refresh)
                        location.reload()
                    },3000)
                }else {
                    elementById.removeAttribute('hidden')
                    elementById.textContent = d.msg
                    setTimeout(() => {
                        pb.removeAttribute('disabled')
                    },1000)
                }
            })
    }else {
        setTimeout(()=>{
            pb.removeAttribute('disabled')
        },1000)
        elementById.removeAttribute('hidden')
        elementById.textContent = 'Please select picture!'
        elementById.style.color = 'red'
    }
})