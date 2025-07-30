# 🌟 Sleep & Habit Tracker

A Python-based personal productivity application that helps users track their daily habits, monitor sleep patterns, and manage to-do lists. Built as a capstone project for Mission Bit.

## ✨ Features

### 💤 Sleep Tracker
- Log daily sleep hours and energy levels
- Visual analysis with matplotlib bar charts showing sleep patterns over time
- Date-based data entry with input validation
- Persistent data storage in CSV format

### ✅ Habit Tracker
- Add and manage personal habits
- Mark habits as completed
- Dynamic habit list management
- Track progress on multiple habits simultaneously

### 📝 To-Do List
- Create and manage daily tasks
- Mark tasks as completed when finished
- Simple, intuitive task management interface

## 🛠️ Technologies Used

- **Python 3.12+** - Core programming language (we used 3.12+)
- **Pandas** - Data manipulation and CSV handling
- **Matplotlib** - Data visualization and charting
- **Tkinter** - Graphical user interface (GUI version)
- **CSV** - Data persistence and storage
- **Datetime** - Date handling and validation

## 🚀 How to Run

### Command-Line Version
```bash
python3 capstone_project_final_cli.py
```

### GUI Version
```bash
python3 tkinter_sleep_tracker.py
```

## 🎯 Key Programming Concepts Demonstrated

- **Object-Oriented Programming**: Class-based GUI architecture
- **File I/O Operations**: CSV reading and writing
- **Data Validation**: Input sanitization and error handling
- **Data Visualization**: Creating meaningful charts with matplotlib
- **User Interface Design**: Both command-line and graphical interfaces
- **Error Handling**: Robust exception handling throughout
- **Code Organization**: Modular function design and clean code practices

## 📋 Requirements

Install required packages:
```bash
pip install pandas matplotlib
```

*Note: tkinter comes pre-installed with most Python distributions*

## 🔧 Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/andreamquiroz/sleep-habit-tracker.git
   cd sleep-habit-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python3 capstone_project_final_cli.py

## 💡 Usage Examples

### Adding Sleep Data
1. Select "Sleep Tracker" from the main menu
2. Choose "Log sleep data"
3. Enter the month and day
4. Input hours of sleep (0-24)
5. Rate your energy level (1-10)
6. Data is automatically saved to CSV

### Viewing Progress
1. Select "View sleep chart" to see your trends
2. Charts display both sleep hours and energy levels over time
3. Data is sorted chronologically for accurate trend analysis

## 🌟 Features Highlights

- **Data Persistence**: All data is saved automatically and persists between sessions
- **Input Validation**: Comprehensive error checking prevents invalid entries
- **Visual Analytics**: Beautiful matplotlib charts provide insights into sleep patterns
- **User-Friendly Interface**: Clean, intuitive design in both CLI and GUI versions
- **Flexible Date Entry**: Easy month/day selection with built-in validation
- **Real-time Feedback**: Immediate confirmation of all user actions

## 🔮 Future Enhancements

- [ ] Data export functionality (PDF reports)
- [ ] Weekly/monthly summary statistics
- [ ] Data backup and sync capabilities
- [ ] Advanced chart types and analytics
