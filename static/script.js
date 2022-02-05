console.log("Hello World");
const form_button = document.getElementById('form-btn');
form_button.addEventListener('click',()=>{

    const xhr = new XMLHttpRequest();
    xhr.open('POST',"/addData",true);
    
    xhr.onload = function(){
        console.log("Hello Ishan")
    }
    xhr.onprogress = function(){
        console.log("kuch to hua hai!")
    }



})