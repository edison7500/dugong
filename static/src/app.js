import Stackedit from 'stackedit-js';

const el = document.querySelector('textarea');
const stackedit = new Stackedit();

// // Open the iframe
// stackedit.openFile({
//     name: 'Filename', // with an optional filename
//     content: {
//       text: el.value // and the Markdown content.
//     }
// }, true);
//
//   // Listen to StackEdit events and apply the changes to the textarea.
// stackedit.on('fileChange', (file) => {
//     el.value = file.content.text;});

/* eslint-disable prefer-arrow-callback, comma-dangle */
/* global Stackedit */

function makeEditButton(el) {
  const div = document.createElement('div');
  div.className = 'stackedit-button-wrapper';
  div.innerHTML = '<a href="javascript:void(0)">Edit with StackEdit</a>';
  el.parentNode.insertBefore(div, el.nextSibling);
  return div.getElementsByTagName('a')[0];
}

const textareaEl = document.querySelector('textarea');
makeEditButton(textareaEl)
  .addEventListener('click', function onClick() {
    const stackedit = new Stackedit();
    stackedit.on('fileChange', function onFileChange(file) {
      textareaEl.value = file.content.text;
    });
    stackedit.openFile({
      name: 'Markdown with StackEdit',
      content: {
        text: textareaEl.value
      }
    });
  });

const htmlEl = document.querySelector('.html');
let markdown = 'Hello **Markdown** writer!';

function doOpen(background) {
  const stackedit = new Stackedit();
  stackedit.on('fileChange', function onFileChange(file) {
    markdown = file.content.text;
    htmlEl.innerHTML = file.content.html;
  });
  stackedit.openFile({
    name: 'HTML with StackEdit',
    content: {
      text: markdown
    }
  }, background);
}

doOpen(true);
makeEditButton(htmlEl)
  .addEventListener('click', function onClick() {
    doOpen(false);
  });