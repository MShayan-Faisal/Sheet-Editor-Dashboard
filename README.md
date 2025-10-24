📊 Sheet-Editor-Dashboard (React.js)

The Sheet-Editor-Dashboard is a responsive and interactive web application built with React.js, designed to view, manage, and edit Google Sheets data directly from a modern dashboard interface.

It allows users to connect to a Google Sheet, edit cell data, add new entries, delete rows, and automatically sync updates in real-time — all from a clean, user-friendly interface.

This project showcases practical use of Google Sheets API integration, React Hooks, and state management to handle live data dynamically.

🚀 Getting Started with Create React App

This project was bootstrapped with Create React App
.

🧰 Available Scripts

In the project directory, you can run:

npm start

Runs the app in the development mode.
Open http://localhost:3000
 to view it in your browser.

The page will reload when you make changes.
You may also see any lint errors in the console.

npm test

Launches the test runner in interactive watch mode.
See the section about running tests
 for more information.

npm run build

Builds the app for production into the build folder.
It bundles React in production mode and optimizes the build for the best performance.

The build is minified, and filenames include hashes.
Your app is ready to be deployed!

For more information, see the section about deployment
.

npm run eject

Note: this is a one-way operation. Once you eject, you can’t go back!

If you need full control over configuration (Webpack, Babel, ESLint, etc.), you can eject to take complete ownership of the build setup.

Most users never need to use eject, as the default configuration is powerful enough for production apps.

🧠 About The Project

The Sheet-Editor-Dashboard provides an intuitive interface to manage spreadsheet data in real-time.
It connects directly to Google Sheets through API calls, allowing instant CRUD (Create, Read, Update, Delete) operations.

Users can:

Fetch and display Google Sheet data in a clean, responsive table

Edit individual cells directly from the UI

Add or delete rows instantly

Sync data automatically with Google Sheets

Manage authentication securely through Google OAuth

This app demonstrates your ability to work with React, APIs, and live data synchronization effectively.

⚙️ Key Features

🔄 Real-time data fetching and synchronization with Google Sheets

✏️ Inline editing for quick cell updates

➕ Add new rows or entries dynamically

❌ Delete rows easily with confirmation

🔍 Search and filter functionality

📱 Responsive dashboard layout

🔐 Secure Google OAuth integration

⚡ Built with modular, reusable React components

🧩 Folder Structure
Sheet-Editor-Dashboard/
│
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Sidebar.jsx
│   │   ├── SheetTable.jsx
│   │   ├── EditModal.jsx
│   │   └── Footer.jsx
│   │
│   ├── utils/
│   │   ├── api.js
│   │   └── sheetService.js
│   │
│   ├── App.jsx
│   ├── App.css
│   ├── index.js
│   └── index.css
│
└── public/
    └── index.html

🧠 What I Learned

Building the Sheet-Editor-Dashboard helped me understand:

How to integrate Google Sheets API with React

Managing form data and state using useState and useEffect

Handling asynchronous data fetching efficiently

Structuring a scalable React component architecture

Implementing real-time data editing in a dashboard UI

Designing a responsive and accessible layout

🚀 Future Improvements

Add dark/light theme toggle

Include chart visualization for data insights

Add multi-sheet management

Enable export/import (CSV, Excel) features

Implement user roles and permissions

Integrate pagination and advanced filtering

🧰 Technologies Used

React.js (Create React App) – Frontend framework

Google Sheets API – Data integration

JavaScript (ES6+) – App logic and event handling

CSS3 / Tailwind CSS / Styled Components – Styling and layout

Axios / Fetch API – For API requests

React Hooks (useState, useEffect) – State and lifecycle management

📬 Contact

Email: shayanrajpoot520@gmail.com

LinkedIn: https://www.linkedin.com/in/m-shayan-faisal/

GitHub: https://github.com/shayan520898

📝 License

This project is open source and available under the MIT License.

📚 Learn More

You can learn more in the Create React App documentation
.
To learn React, check out the React documentation
.
