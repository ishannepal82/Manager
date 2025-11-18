Python File Organizer (MVP)

The Python File Organizer is a lightweight, automated tool designed to keep your system clean by monitoring specific directories and sorting files into organized subfolders. It focuses on simplicity, reliability, and minimal configuration while still providing the core features needed for day-to-day file management. This tool is ideal for users who frequently download, create, or move files and want an automated way to maintain an uncluttered workspace without using heavy or complex software.

Features

Real-time file detection – Automatically detects file creation and deletion events in user-selected folders such as Downloads and Desktop.

Automatic sorting – Files are categorized based on their extension (e.g., images, documents, archives) and moved into pre-defined subfolders.

Configurable rules – File type rules are defined in a simple JSON file, allowing you to easily modify or expand your organizer without touching code.

Lightweight architecture – No GUI or unnecessary layers. The tool focuses purely on performance and simplicity.

Desktop & Downloads cleanup – Keeps these commonly cluttered folders neatly structured with subdirectories such as Images, Documents, and Archives.

How It Works

The organizer continuously watches selected directories for changes. When a new file appears, it checks its file extension against the rules defined in rules.json. Based on the category, it moves the file into the appropriate subfolder. Unknown file types can be directed to a generic “Others” or “Unknown” folder.

Project Structure

The project includes separate modules for watching directories, handling events, sorting logic, and moving files. This modular structure keeps the code clean, maintainable, and easy to extend.

Why This Project Exists

This organizer is built as a personal MVP to automate repetitive housekeeping tasks, reduce clutter, and maintain a tidy workspace without overwhelming features. It’s simple, effective, and customizable.