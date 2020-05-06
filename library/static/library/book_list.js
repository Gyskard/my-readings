const checkRead = document.getElementById('checkRead');
const checkUnread = document.getElementById('checkUnread');
const bookRead = document.getElementsByClassName("read");
const bookUnread = document.getElementsByClassName("unread");

checkRead.addEventListener('change', (event) => {
    if (event.target.checked) {
        for (let i = 0; i < bookRead.length; i++) {
            bookRead[i].style.display = "list-item"
        }
    }
    else {
        for (let i = 0; i < bookRead.length; i++) {
            bookRead[i].style.display = "none"
        }
    }
})

checkUnread.addEventListener('change', (event) => {
    if (event.target.checked) {
        for (let i = 0; i < bookUnread.length; i++) {
            bookUnread[i].style.display = "list-item"
        }
    }
    else {
        for (let i = 0; i < bookUnread.length; i++) {
            bookUnread[i].style.display = "none"
        }
    }
})