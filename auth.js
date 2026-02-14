// 登录状态检查
function checkLogin() {
    const isLoggedIn = localStorage.getItem('userLoginStatus') === 'true';
    const currentPage = window.location.pathname.split('/').pop();

    // 如果未登录且当前页面不是登录页，跳转到登录页
    if (!isLoggedIn && currentPage !== 'index.html') {
        window.location.href = 'index.html';
        return false;
    }

    // 如果已登录且当前页面是登录页，跳转到首页
    if (isLoggedIn && currentPage === 'index.html') {
        window.location.href = 'shouye.html';
        return false;
    }

    return true;
}

// 页面加载时检查
document.addEventListener('DOMContentLoaded', function() {
    if (!checkLogin()) return;

    // 显示用户信息（仅在非登录页显示）
    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage !== 'index.html') {
        const userName = localStorage.getItem('userName');
        if (userName) {
            // 在导航栏显示用户信息
            const nav = document.querySelector('.nav');
            if (nav) {
                // 检查是否已经存在用户信息div
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

// 退出登录
function logout() {
    localStorage.removeItem('userLoginStatus');
    localStorage.removeItem('userName');
    window.location.href = 'index.html';
}