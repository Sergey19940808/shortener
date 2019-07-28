'use strict';

const short_links = document.querySelectorAll('.link_table');
const origin_links = document.querySelectorAll('.link_table-origin');

short_links.forEach(link=> {
    link.addEventListener('click', (event) => handlerShortLink(event));
    link.removeEventListener('click', (event) => handlerShortLink(event));
});
origin_links.forEach(link=> {
    link.addEventListener('click', (event) => handlerOriginLink(event));
    link.removeEventListener('click', (event) => handlerOriginLink(event));
});

const handlerShortLink = (event) => {
  event.preventDefault();
  const idShortener = parseInt(event.target.dataset.id);
  fetch('/shortener/count/'+idShortener).then((response)=> {
      location.reload();
      window.open(event.target.href, '_blank');
  })
};

const handlerOriginLink = (event) => {
  event.preventDefault();
  window.open(event.target.href, '_blank');
};
