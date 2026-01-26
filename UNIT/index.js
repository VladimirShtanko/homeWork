const wrURL = 'wss://echo-ws-service.herokuapp.com';

const area = document.querySelector('.messageTable__area');
const inputs = document.getElementById('input');
const sendBtn = document.querySelector('.send');
const geoBtn = document.querySelector('.geolocation');

let websoket;

function newWebsoket(){
    websoket = new WebSocket(wrURL);
    websoket.message = function(event){
        writeMyMessage(event.data, 'serMess')
    }

}

function writeMyMessage(message, clas ){
    const pre = document.createElement('div')
    pre.classList.add(clas)
    pre.textContent = message;
    area.appendChild(pre);
}

sendBtn.addEventListener('click', ()=>{
    const message = inputs.value;
    inputs.innerHTML = '';
   
    writeMyMessage(`Вы: ${message}` , 'myMes')
    websoket.send(message)
    
    
})

function sendLocation (){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition((position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const locationMessage = ` https://www.openstreetmap.org/#map=8/${lat}/${lon}`;
            websoket.send(locationMessage)
        }, (error) =>{
            alert(error.message)
        })
    }else{
        alert('Геолокация не доступна')
    }
}















































