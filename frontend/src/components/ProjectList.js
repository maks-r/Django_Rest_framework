import React from 'react'


const ProjectItem = ({project}) => {
    return (
    <tr>
        <td>{project.name}</td>
        <td>{project.repository}</td>
        <td>{project.users}</td>
    </tr>
    )
}

const ProjectList = ({projects}) =>  {
    return (
        <table>
        <th>
            name
        </th>
        <th>
            users
        </th>
        <th>
            repository
        </th>
        {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList