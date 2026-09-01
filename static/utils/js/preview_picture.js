/**
 * 图片预览
 * @param {string} file_input_id 文件输入框id
 * @param {string} el_img_id img element id
 * @param {string} hidden_id 是否有隐藏属性 Attribute 有就写上id，没就不写
 */
export function preview_picture(file_input_id, el_img_id, hidden_id='0'){
    document.getElementById(file_input_id).addEventListener('change', function (e){
        const file = this.files[0]
        if (file && file.type.startsWith('image/')){
            const reader = new FileReader()
            reader.onload = function (event){
                const preview = document.getElementById(el_img_id)
                preview.src = event.target.result
                if (hidden_id !== '0'){
                    if (el_img_id === hidden_id){
                        preview.hidden = false
                    }else {
                        document.getElementById(hidden_id).removeAttribute('hidden')
                    }
                }
            }
            reader.readAsDataURL(file)
        }
    })
}