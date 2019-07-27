'use strict';
const links = document.querySelectorAll('.link_table');

links.forEach(link=> {

    link.addEventListener('click', (event) => handlerCount(event));
    link.removeEventListener('click', (event) => handlerCount(event));
});

const handlerCount = (event) => {
  event.preventDefault();
  const idShortener = parseInt(event.target.dataset.id);
  fetch('/shortener/count/'+idShortener).then((response)=> {
      location.reload();
      window.open(event.target.href, '_blank');
  })
};