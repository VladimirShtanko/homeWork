const btn = document.querySelector('.btn').addEventListener('click', renderImage)


async function renderImage (event){
event.preventDefault();
const imagGallery = document.getElementById('imageGallery');
const loader = document.querySelector('.loader');
imagGallery.innerHTML='';
loader.style.display = 'block';

try{
    const response = await fetch('https://dog.ceo/api/breeds/image/random/30');
    if(!response.ok){
        throw new Error('Сетевая ошибка' )
    }  
    const data = await response.json();
    if(data && Array.isArray(data.message)){  

        displayRender(data.message);
    }
    
}
catch(e){
    console.error(e.message)
}
finally{
    loader.style.display = 'none';
}


}

function displayRender(imagesUrl){
    const reImage = document.getElementById('imageGallery');
    imagesUrl.forEach(image => {
    const imgEm = document.createElement('img');
    imgEm.src = image;
    imgEm.alt = 'картинки с сайта';
    imgEm.class = 'img'
    imgEm.classList.add('gallery__img');
    reImage.appendChild(imgEm)
    });
}