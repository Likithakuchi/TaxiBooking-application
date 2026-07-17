// Base URL for the Django backend API
const API_BASE_URL = 'http://127.0.0.1:8000';

// Helper function to handle API calls
async function apiFetch(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    
    // Set default headers for JSON payload
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
    };
    
    const config = {
        ...options,
        headers,
    };
    
    if (config.body && typeof config.body === 'object') {
        config.body = JSON.stringify(config.body);
    }
    
    try {
        const response = await fetch(url, config);
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || data.detail || `Request failed with status ${response.status}`);
        }
        return data;
    } catch (error) {
        console.error(`API Error (${endpoint}):`, error);
        throw error;
    }
}

// Toast notification system
function showToast(message, type = 'info') {
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        document.body.appendChild(toastContainer);
    }
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span>${message}</span>
    `;
    
    toastContainer.appendChild(toast);
    
    // Trigger animation
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);
    
    // Remove toast after 4 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            toast.remove();
        }, 400);
    }, 4000);
}

// User state helper functions
const Session = {
    getUser() {
        const userStr = localStorage.getItem('taxi_user');
        return userStr ? JSON.parse(userStr) : null;
    },
    setUser(user, role) {
        localStorage.setItem('taxi_user', JSON.stringify({ ...user, role }));
    },
    clear() {
        localStorage.removeItem('taxi_user');
    },
    isLoggedIn() {
        return this.getUser() !== null;
    },
    getRole() {
        const user = this.getUser();
        return user ? user.role : null;
    }
};

// Toggle Theme (Light vs Dark)
function toggleTheme() {
    const body = document.body;
    body.classList.toggle('light-theme');
    const isLight = body.classList.contains('light-theme');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    
    // Update toggle button icon
    const btn = document.getElementById('btn-theme-toggle');
    if (btn) {
        btn.innerText = isLight ? '🌙' : '☀️';
    }
}

// Load theme state on start
function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const body = document.body;
    if (savedTheme === 'light') {
        body.classList.add('light-theme');
    } else {
        body.classList.remove('light-theme');
    }
}

// Auto-inject components on load
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    injectNavbar();
    injectFooter();
    
    // Set initial toggle button text after rendering navbar
    const btn = document.getElementById('btn-theme-toggle');
    if (btn) {
        btn.innerText = document.body.classList.contains('light-theme') ? '🌙' : '☀️';
    }
});

// Render dynamic navbar
function injectNavbar() {
    const header = document.querySelector('header');
    if (!header) return;
    
    const isLoggedIn = Session.isLoggedIn();
    const role = Session.getRole();
    const user = Session.getUser();
    
    let logoUrl = 'index.html';
    let navLinksHTML = `<li><a href="index.html" id="nav-home">Home</a></li>`;
    
    if (isLoggedIn) {
        if (role === 'customer') {
            navLinksHTML += `
                <li><a href="booking.html" id="nav-book">Book a Ride</a></li>
                <li><a href="ride_history.html" id="nav-history">Ride History</a></li>
                <li><a href="customer_dashboard.html" id="nav-cust-dash">Customer Dashboard</a></li>
            `;
        } else if (role === 'driver') {
            navLinksHTML += `
                <li><a href="driver_dashboard.html" id="nav-driver-dash">Driver Dashboard</a></li>
                <li><a href="drivers.html" id="nav-driver-details">Driver Details</a></li>
            `;
        } else if (role === 'admin') {
            navLinksHTML += `
                <li><a href="admin_dashboard.html" id="nav-admin-dash">Admin Dashboard</a></li>
            `;
        }
    } else {
        navLinksHTML += `
            <li><a href="drivers.html" id="nav-driver-reg">Become a Driver</a></li>
        `;
    }
    
    let authHTML = '';
    if (isLoggedIn) {
        const initial = user.full_name ? user.full_name.charAt(0) : (user.driver_name ? user.driver_name.charAt(0) : 'A');
        const displayName = user.full_name || user.driver_name || 'Admin';
        authHTML = `
            <div class="user-profile-widget">
                <div class="avatar">${initial.toUpperCase()}</div>
                <span style="font-size: 0.85rem; font-weight: 500; max-width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${displayName}</span>
                <button onclick="handleLogout()" class="btn btn-secondary btn-sm" style="padding: 0.3rem 0.6rem; font-size: 0.75rem;">Logout</button>
            </div>
        `;
    } else {
        authHTML = `
            <a href="login.html" class="btn btn-secondary btn-sm">Sign In</a>
            <a href="register.html" class="btn btn-primary btn-sm">Register</a>
        `;
    }
    
    header.innerHTML = `
        <div class="nav-container">
            <a href="${logoUrl}" class="logo">
                <span>Cab</span>Flow
            </a>
            <ul class="nav-links">
                ${navLinksHTML}
            </ul>
            <div class="nav-auth">
                <button onclick="toggleTheme()" class="btn" id="btn-theme-toggle" style="padding: 0.4rem; font-size: 1rem; border-radius: 50%; min-width: 32px; height: 32px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--border-color); background: transparent; cursor: pointer;">☀️</button>
                ${authHTML}
            </div>
        </div>
    `;
    
    // Mark active link
    const path = window.location.pathname;
    const filename = path.substring(path.lastIndexOf('/') + 1) || 'index.html';
    
    const linkMap = {
        'index.html': 'nav-home',
        'booking.html': 'nav-book',
        'ride_history.html': 'nav-history',
        'customer_dashboard.html': 'nav-cust-dash',
        'driver_dashboard.html': 'nav-driver-dash',
        'admin_dashboard.html': 'nav-admin-dash',
        'drivers.html': role === 'driver' ? 'nav-driver-details' : 'nav-driver-reg',
    };
    
    const activeId = linkMap[filename];
    if (activeId) {
        const activeLink = document.getElementById(activeId);
        if (activeLink) activeLink.classList.add('active');
    }
}

// Render footer
function injectFooter() {
    const footer = document.querySelector('footer');
    if (!footer) return;
    
    footer.innerHTML = `
        <div class="footer-content">
            <p>&copy; 2026 CabFlow Taxi Booking Platform. Built using HTML5, CSS3, ES6 & Django REST Framework.</p>
        </div>
    `;
}

// Perform Logout
function handleLogout() {
    Session.clear();
    showToast('Logged out successfully!', 'info');
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 800);
}

// Enforce role-based access control
function enforceRole(allowedRoles) {
    const user = Session.getUser();
    if (!user) {
        showToast('Access denied. Please sign in first.', 'warning');
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 1000);
        return false;
    }
    if (!allowedRoles.includes(user.role)) {
        showToast(`Access denied. This page is restricted to ${allowedRoles.join(' or ')} accounts.`, 'danger');
        setTimeout(() => {
            if (user.role === 'customer') window.location.href = 'customer_dashboard.html';
            else if (user.role === 'driver') window.location.href = 'driver_dashboard.html';
            else if (user.role === 'admin') window.location.href = 'admin_dashboard.html';
            else window.location.href = 'index.html';
        }, 1500);
        return false;
    }
    return true;
}

