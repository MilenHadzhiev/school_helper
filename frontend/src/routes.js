// import Base from 'antd/lib/typography/Base';
import React from 'react';
import { Route } from 'react-router-dom';

import LessonsList from './containers/LessonsListView';
import LessonsDetail from './containers/LessonDetailView';

const BaseRouter = () => {
    return (
        <div>
            <Route exact path='/' component={LessonsList} />
            <Route exact path='/:lessonID' component={LessonsDetail} />
        </div>
    )
};

export default BaseRouter;