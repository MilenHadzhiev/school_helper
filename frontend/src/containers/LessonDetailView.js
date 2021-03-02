import React from 'react';
import axios from 'axios';
// import Lesson from '../components/Lesson';

import { Card } from 'antd';

class LessonsDetail extends React.Component {

    state = {
        lesson: {},
    }

    componentDidMount() {
        const lessonID = this.props.match.params.lessonID;
        axios.get(`http://localhost:8000/api/${lessonID}`)
            .then(res => {
                this.setState({
                    lesson: res.data,
                });
            })
    }

    render() {
        return (
            <Card title={this.state.lesson.title}> 
                <p>{this.state.lesson.content}</p>
            </Card>
        );
    }
}

export default LessonsDetail;