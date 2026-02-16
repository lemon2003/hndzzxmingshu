function checkLogin() {
    const isLoggedIn = localStorage.getItem('userLoginStatus') === 'true';
    const currentPage = window.location.pathname.split('/').pop();
    if (!isLoggedIn && currentPage !== '../index.html') {
        window.location.href = '../index.html';
        return false;
    }
    if (isLoggedIn && currentPage === '../index.html') {
        window.location.href = '../shouye.html';
        return false;
    }
    return true;
}
document.addEventListener('DOMContentLoaded', function() {
    if (!checkLogin()) return;
    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage !== '../index.html') {
        const userName = localStorage.getItem('userName');
        if (userName) {
            const nav = document.querySelector('.nav');
            if (nav) {
                let userDiv = nav.querySelector('.user-info');
                if (!userDiv) {
                    userDiv = document.createElement('div');
                    userDiv.className = 'user-info';
                    userDiv.innerHTML = `
                        <span style="color: #2c5282; margin-right: 20px;">欢迎，${userName}</span>
                        <a href="#" onclick="logout()" style="color: #ff6b6b;">退出</a>
                    `;
                    nav.appendChild(userDiv);
                }
            }
        }
    }
});
function logout() {
    localStorage.removeItem('userLoginStatus');
    localStorage.removeItem('userName');
    window.location.href = '../index.html';
}