import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project': '',
            'text': []
        }
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.project, this.state.text)
        event.preventDefault()
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }


     handleProjectChange(event) {
        if (!event.target.selectedOptions) {
            return
        }

        let projects = []

        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            projects.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'projects': projects
        })
    }

    render() {
        return (
        <form onSubmit={(event) => this.handleSubmit(event)}>
            <input type="text" name="text" placeholder="text" value={this.state.text} onChange={(event) => this.handleChange(event)} />
            <select multiple onChange={(event) => this.handleProjectChange(event)}>
                {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
            </select>
            <input type="submit" value="Create"/>
        </form>
        )
    }
}

export default ToDoForm;