import {preview_picture} from "/static/utils/js/preview_picture.js";

const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

// document.getElementById('upload-flower-pic')
//     .addEventListener('change',function (e){
//         const file = this.files[0]
//         if (file && file.type.startsWith('image/')){
//             const reader = new FileReader()
//             reader.onload = function (event){
//                 const preview = document.getElementById('pic-preview')
//                 preview.src = event.target.result
//                 preview.removeAttribute('hidden')
//             }
//             reader.readAsDataURL(file)
//         }
// })
preview_picture('upload-flower-pic', 'pic-preview','pic-preview')

document.getElementById('form-upload-flowers').addEventListener('submit', function (e){
    e.preventDefault()
    let form_data = new FormData(this)
    for (const [d,v] of form_data) {
        console.log(d,':',v)
    }
    let tip = document.getElementById('upload-flower-tip');
    if(!form_data.get('flower_name') || document.getElementById('upload-flower-pic').files.length === 0){
        tip.removeAttribute('hidden')
    }else {
        fetch('/user/upload',{
            method: 'post',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token
            }
        }).then(res => res.json())
            .then(d => {
                if (d.status === 200){
                    tip.removeAttribute('hidden')
                    tip.textContent = d.msg
                }else {
                    tip.removeAttribute('hidden')
                    tip.textContent = d.msg
                }
            })
    }
})

preview_picture('change-flower-pic', 'pic-preview-change', 'pic-preview-change')

document.getElementById('form-change-flowers').addEventListener('submit', function (e){
    e.preventDefault()
    const form_data = new FormData(this)
    for (const [d,v] of form_data) {
        console.log(d,':',v)
    //     if (!['form_upload_data ', 'csrfmiddlewaretoken'].includes(d)){
    //
    //     }
    }
    // let value = this.querySelector('input')
    // console.log(value.value)
})