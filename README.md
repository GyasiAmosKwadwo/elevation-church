# Elevation Church

A full-stack web application for Elevation Church, featuring a responsive frontend built with React and TypeScript, and a robust backend API powered by Django REST Framework.

## Features

### Frontend (Client)
- **Modern UI**: Built with React, TypeScript, and Tailwind CSS for a responsive and accessible user interface.
- **Components**: Reusable UI components including accordions, buttons, cards, forms, and more.
- **Pages**: Dedicated pages for Home, Sermons, Series, Events, Admin dashboard, and more.
- **Routing**: Client-side routing with React Router for seamless navigation.
- **State Management**: Context API for managing application state.
- **Icons and Styling**: Customizable icons and consistent styling with Tailwind CSS.

### Backend (Server)
- **API**: RESTful API built with Django REST Framework (DRF) for handling church data.
- **Models**: Comprehensive data models for Sermons, Series, Events, Devotions, Reflections, Prayer Requests, Announcements, and Live Streams.
- **Authentication**: JWT-based authentication using Simple JWT and Djoser for user management.
- **Media Storage**: Cloudinary integration for efficient media file storage and serving.
- **Database**: PostgreSQL database with UUID primary keys for scalability.
- **Documentation**: API documentation with DRF Spectacular (Swagger/OpenAPI).
- **CORS**: Configured for cross-origin requests to support the frontend.

## Tech Stack

### Frontend
- **React**: 18.x
- **TypeScript**: For type safety
- **Vite**: Build tool for fast development
- **Tailwind CSS**: Utility-first CSS framework
- **React Router**: Client-side routing
- **Lucide React**: Icon library
- **Axios**: HTTP client for API calls

### Backend
- **Django**: 5.2.6
- **Django REST Framework**: 3.16.1
- **PostgreSQL**: Database
- **Cloudinary**: Media storage
- **Simple JWT**: Authentication
- **Djoser**: User management
- **DRF Spectacular**: API documentation
- **Gunicorn**: WSGI server for production

## Getting Started

### Prerequisites
- Node.js (18.x or higher)
- Python (3.11 or higher)
- PostgreSQL
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/elevation-church.git
   cd elevation-church
   ```

2. **Backend Setup:**
   ```bash
   cd server/core
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Create a `.env` file in `server/core/` with:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_URL=postgresql://user:password@localhost:5432/dbname
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   ```

4. **Database Migration:**
   ```bash
   python manage.py migrate
   ```

5. **Run Backend:**
   ```bash
   python manage.py runserver
   ```

6. **Frontend Setup (in a new terminal):**
   ```bash
   cd client
   npm install
   npm run dev
   ```

7. **Access the Application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/api/schema/swagger-ui/

## Project Structure

```
elevation-church/
├── client/                 # Frontend React application
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── context/        # React context for state management
│   │   ├── hooks/          # Custom React hooks
│   │   └── lib/            # Utility functions
│   ├── public/             # Static assets
│   └── vite.config.ts      # Vite configuration
├── server/                 # Backend Django application
│   └── core/
│       ├── api/            # Django app for API
│       │   ├── models.py   # Database models
│       │   ├── views.py    # API views
│       │   ├── serializers.py # DRF serializers
│       │   └── urls/       # URL configurations
│       ├── core/           # Django project settings
│       │   ├── settings.py # Main settings
│       │   ├── urls.py     # Root URL configuration
│       │   └── wsgi.py     # WSGI configuration
│       ├── media/          # Media files (development)
│       ├── staticfiles/    # Collected static files
│       └── requirements.txt # Python dependencies
└── README.md
```

## API Endpoints

- **Sermons**: `/api/sermons/`
- **Series**: `/api/series/`
- **Events**: `/api/events/`
- **Devotions**: `/api/devotions/`
- **Reflections**: `/api/reflections/`
- **Prayer Requests**: `/api/prayer-requests/`
- **Announcements**: `/api/announcements/`
- **Live Streams**: `/api/live-streams/`
- **Authentication**: `/auth/` (via Djoser)

## Deployment

### Frontend (Vercel)
1. Connect your GitHub repository to Vercel.
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Deploy.

### Backend (Render)
1. Create a new Web Service on Render.
2. Connect your GitHub repository.
3. Set build command: `./build.sh`
4. Set start command: `gunicorn core.wsgi:application`
5. Add environment variables.
6. Deploy.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact the development team.
