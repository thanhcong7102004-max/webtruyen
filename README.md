# WebTruyen - Web Novel Platform

A PHP-based web application for reading, managing, and sharing web novels (light novels/web stories). The platform provides both frontend and backend functionality with user authentication, story management, and community features.

## Project Overview

WebTruyen is a full-stack web application built with PHP and MySQL that allows users to:
- Browse and read web novels/stories
- Search and filter stories by genre
- Track reading history and bookmarks
- Leave comments on chapters
- Follow favorite authors and stories
- Manage reading preferences

## Features

### User Features
- **User Authentication**: Registration, login, and logout functionality
- **Story Browsing**: View stories organized by categories/genres
- **Search & Filter**: Search stories by title, author, or category
- **Reading History**: Track previously read stories and chapters
- **Bookmarks & Favorites**: Save favorite stories for quick access
- **Comments**: Leave comments on chapters and interact with other readers
- **Follow System**: Follow favorite stories and authors
- **Notifications**: Receive updates on followed stories

### Admin Features
- **User Management**: Create, view, update, and delete user accounts
- **Story Management**: Add, edit, and delete stories
- **Chapter Management**: Manage chapters for each story
- **Category Management**: Create and manage story categories/genres
- **Comment Moderation**: View and manage user comments
- **Dashboard & Analytics**: View statistics and analytics

## Project Structure

```
webtruyen/
├── web/                          # Main web application
│   ├── frontend/                 # Frontend pages
│   │   ├── index.php            # Home page
│   │   └── story.php            # Story detail page
│   ├── admin/                   # Admin panel
│   │   ├── back_end/            # Backend management
│   │   │   ├── quanlytruyen/    # Story management
│   │   │   ├── quanlychuong/    # Chapter management
│   │   │   ├── quanlyuser/      # User management
│   │   │   ├── quanlytheloai/   # Category management
│   │   │   └── quanlybinhluan/  # Comment moderation
│   │   └── database/            # Database helpers
│   ├── database.php             # Database connection
│   ├── Trangchu.php             # Home page
│   ├── truyen.php               # Story list page
│   ├── theloai.php              # Category/Genre page
│   ├── timkiem1.php             # Search page
│   ├── yeuthich.php             # Favorites page
│   ├── lichsu.php               # History page
│   ├── theodoi.php              # Following page
│   ├── binhluan.php             # Comments page
│   ├── thongbao.php             # Notifications page
│   ├── dangky.php               # Registration page
│   ├── dangnhap.php             # Login page
│   ├── dangxuat.php             # Logout page
│   ├── quenmk.php               # Forgot password page
│   ├── header.php               # Header component
│   ├── footer.php               # Footer component
│   ├── menu_backend.php         # Admin menu
│   └── style.css                # Main styles
├── public/                       # Public assets
│   └── giaodien/
│       └── images/              # Images and graphics
└── README.md                     # This file
```

## Database Schema

The application uses MySQL database named `truyenhaytt` with the following main tables:

- **users**: User accounts and authentication
- **truyen** (stories): Story information
- **chuong** (chapters): Story chapters
- **theloai** (categories): Story categories/genres
- **binhluan** (comments): User comments on chapters
- **lichsu** (history): User reading history
- **theodoi** (follows): User follow relationships
- **yeuthich** (favorites): User favorite stories
- **thongbao** (notifications): User notifications

## Installation & Setup

### Prerequisites
- PHP 7.0 or higher
- MySQL 5.7 or higher
- XAMPP or similar local server environment
- Apache web server

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanhcong7102004-max/webtruyen.git
   ```

2. **Setup local environment**
   - Place the project in `C:\xampp\htdocs\webtruyen` (for XAMPP)
   - Or your web server's document root

3. **Create the database**
   - Open phpMyAdmin: `http://localhost/phpmyadmin`
   - Create a new database named `truyenhaytt`
   - Import the database schema (if provided)

4. **Configure database connection**
   - Edit [web/database.php](web/database.php)
   - Update database credentials if needed:
     ```php
     $servername = "localhost";
     $username = "root";
     $password = "";
     $dbname = "truyenhaytt";
     ```

5. **Access the application**
   - Frontend: `http://localhost/webtruyen/web/Trangchu.php`
   - Admin Panel: `http://localhost/webtruyen/web/admin/`

## Core Pages & Functionality

### Frontend Pages
| Page | File | Description |
|------|------|-------------|
| Home | `Trangchu.php` | Homepage with featured stories |
| Stories | `truyen.php` | Browse all stories |
| Categories | `theloai.php` | Browse stories by category |
| Search | `timkiem1.php` | Search and filter stories |
| Reading History | `lichsu.php` | View previously read stories |
| Favorites | `yeuthich.php` | View bookmarked stories |
| Following | `theodoi.php` | View followed stories |
| Notifications | `thongbao.php` | View updates and notifications |
| Comments | `binhluan.php` | View and leave comments |

### Authentication Pages
- `dangky.php` - User registration
- `dangnhap.php` - User login
- `dangxuat.php` - User logout
- `quenmk.php` - Password recovery

## Key Database Files

- [web/database/db_truyen.php](web/database/db_truyen.php) - Story database queries
- [web/database/db_user.php](web/database/db_user.php) - User database queries
- [web/database/db_theloai.php](web/database/db_theloai.php) - Category database queries

## Admin Management Modules

Located in `web/admin/back_end/`:

1. **Story Management** (`quanlytruyen/`)
   - List stories: `quanlytruyen.php`
   - Add story: `themtruyen.php`
   - Edit story: `suatruyen.php`
   - Delete story: `xoatruyen.php`

2. **Chapter Management** (`quanlychuong/`)
   - Add chapter: `themchuong.php`
   - Edit chapter: `suachuong.php`
   - Delete chapter: `xoachuong.php`
   - Manage chapters: `quanlychuong.php`

3. **User Management** (`quanlyuser/`)
   - List users: `quanlyuser.php`
   - Add user: `themuser.php`
   - Edit user: `suauser.php`
   - Delete user: `xoauser.php`

4. **Category Management** (`quanlytheloai/`)
   - List categories: `quanlytheloai.php`
   - Edit category: `suatheloai.php`

5. **Comment Moderation** (`quanlybinhluan/`)
   - Manage comments: `quanlybinhluan.php`

## Technologies Used

- **Backend**: PHP (Server-side logic)
- **Database**: MySQL (Data storage)
- **Frontend**: HTML, CSS, JavaScript
- **Server**: Apache (with XAMPP)
- **Version Control**: Git

## File Organization

- **PHP Files**: Server-side logic and page rendering
- **CSS Files**: Website styling
- **HTML Files**: Static HTML templates (if any)
- **Public/Images**: Website images and assets
- **Python Scripts**: Utility scripts (e.g., `fix_html_structure.py`)

## Session Management

The application uses PHP sessions for user authentication and state management. Session variables are used to track:
- Logged-in user information
- User preferences
- Reading progress

## Security Considerations

When deploying to production:
1. Change default database credentials
2. Implement input validation and sanitization
3. Use parameterized queries to prevent SQL injection
4. Implement HTTPS
5. Add CSRF protection tokens
6. Secure password hashing (use `password_hash()` and `password_verify()`)
7. Implement rate limiting for authentication
8. Validate and sanitize all user inputs

## Future Enhancements

- Mobile app version
- Advanced recommendation system
- Social features (user profiles, messaging)
- Reading progress tracking
- Offline reading capability
- Multi-language support
- API for third-party integrations
- Performance optimization and caching

## License

This project is proprietary. All rights reserved.

## Contact & Support

For issues, questions, or contributions, please contact the project owner or submit issues through the repository.

## Changelog

### Current Version
- Initial project structure
- Basic user authentication
- Story browsing and reading
- Admin management panel
- Comment system
- Search and filter functionality

---
#PHP ; #CSS, #HTML ; #MySQL 

**Last Updated**: December 2025  
**Status**: In Development
