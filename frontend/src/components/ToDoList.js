import React from 'react'


const ToDoItem = ({todo}) => {
    return (
    <tr>
        <td>{todo.project}</td>
        <td>{todo.text}</td>
        <td>{todo.create}</td>
        <td>{todo.update}</td>
        <td>{todo.creator}</td>
    </tr>
    )
}

const ToDoList = ({todos}) =>  {
    return (
        <table>
        <th>
            name
        </th>
        <th>
            user
        </th>
        {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDoList