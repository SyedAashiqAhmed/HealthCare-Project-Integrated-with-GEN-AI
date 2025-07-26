# 🏥 Healthcare Appointment System

A comprehensive Doctor-Patient Appointment Management System built with Flask and Python.

## 🚀 Features

### For Patients:
- **User Registration & Login**: Secure authentication system
- **Appointment Booking**: Easy-to-use form to book doctor appointments
- **Symptom Description**: Detailed symptom input for better diagnosis
- **Appointment Status Check**: Check appointment status using username
- **Multiple Doctor Selection**: Choose from available doctors

### For Doctors:
- **Appointment Dashboard**: View all patient appointments
- **Patient Details**: See patient name, symptoms, date, and time
- **Status Management**: Accept or reject appointments
- **Real-time Updates**: Instant status updates in the database

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: JSON file (db.json)
- **Authentication**: Session-based login system

## 📁 Project Structure

```
HealthCare Project/
├── patient.py          # Patient portal Flask app
├── doc.py             # Doctor portal Flask app
├── op.py              # Main application with authentication
├── db.json            # Database file (users & appointments)
├── dq.html            # Enhanced appointment booking page
├── templates/         # HTML templates
│   ├── login.html
│   ├── signup.html
│   ├── patient_home.html
│   └── doctor.html
├── static/            # Static files
│   └── image.png
└── bot/               # Additional bot functionality
    ├── app.py
    └── templates/
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Flask

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <HealthCare-Project-Integrated-with-GEN-AI>
   cd HealthCare-Project
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**

   **Option 1: Run main application (with authentication)**
   ```bash
   python op.py
   ```
   Access at: http://localhost:5000

   **Option 2: Run patient portal only**
   ```bash
   python patient.py
   ```
   Access at: http://localhost:5000

   **Option 3: Run doctor portal only**
   ```bash
   python doc.py
   ```
   Access at: http://localhost:5001

## 📋 Usage Guide

### For Patients:
1. **Register/Login**: Create an account or login with existing credentials
2. **Book Appointment**: Fill the appointment form with your details
3. **Check Status**: Use your username to check appointment status

### For Doctors:
1. **Access Portal**: Open the doctor portal
2. **View Appointments**: See all pending and processed appointments
3. **Manage Status**: Accept or reject appointments as needed

## 🔧 Configuration

The system uses `db.json` for data storage with the following structure:

```json
{
  "users": {
    "username": "password"
  },
  "appointments": [
    {
      "username": "patient_username",
      "doctor": "Dr. Name",
      "date": "YYYY-MM-DD",
      "time": "HH:MM",
      "symptoms": "patient symptoms",
      "status": "pending/accepted/rejected"
    }
  ]
}
```

## 🎯 Key Features

- ✅ **Secure Authentication**: User registration and login system
- ✅ **Appointment Management**: Complete CRUD operations for appointments
- ✅ **Real-time Status Updates**: Instant status changes reflected in database
- ✅ **Responsive Design**: Works on desktop and mobile devices
- ✅ **Data Persistence**: All data stored in JSON format
- ✅ **Multi-user Support**: Multiple patients and doctors can use the system

## 🔒 Security Features

- Password-based authentication
- Session management
- Input validation
- SQL injection prevention (using JSON instead of SQL)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 👥 Authors

-Syed Aashiq Ahmed - [YourGitHub](https://github.com/SyedAashiqAhmed)

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- All contributors and testers

---

**Note**: This is a demonstration project. For production use, consider implementing additional security measures and using a proper database system. 
