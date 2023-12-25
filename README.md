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

# API requests
Get all projects belonging to group associated with project id bf19998f-8b9c-407b-82c9-1ca6f362c9c6
/api/v1/projects/bf19998f-8b9c-407b-82c9-1ca6f362c9c6/groups

Get all projects belonging to group 1
/api/v1/groups/1/projects