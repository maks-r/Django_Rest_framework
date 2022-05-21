import React from 'react'


const ToDoItem = ({todo, project, deleteToDo}) => {
    let projectStr = todo.project.map(projectId => project.find(p => p.id == projectId ).name)
    return (
    <tr>
        <td>{todo.project.map(projectId => project.find(p => p.id == projectId ).name)}</td>
        <td>{todo.text}</td>
        <td>{todo.create}</td>
        <td>{todo.update}</td>
        <td>{todo.creator}</td>
        <td><button onClick={()=>deleteToDo(todo.id)}>Delete</button></td>
    </tr>
    )
}

const ToDoList = ({todos, project, deleteToDo}) =>  {
    return (
        <table>
        <th>
            Project
        </th>
        <th>
            Text
        </th>
        <th>
            Create
        </th>
        <th>
            Update
        </th>
        <th>
            Creator
        </th>
        {todos.map((todo) => <ToDoItem todo={todo} project={project} deleteToDo={deleteToDo}/>)}
        </table>
    )
}

export default ToDoList