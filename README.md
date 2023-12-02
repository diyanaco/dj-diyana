# dj-diyana
A backend api in django rest framework for Diyana Task Management System

# Workflow
1. Create Project
   1. Create task
      1. Create subtask
   2. Group task into list
2. Create phases for the project
   1. On each phase, create task
   2. Group phases into template_phases
3. Create phases from template_phases
   1. Create the tree structure of task, subtask, tasklist
   2. Newly created task,subtask,tasklist will have auto prefilled name