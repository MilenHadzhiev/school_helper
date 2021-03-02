import React from 'react';
// import axios from 'axios';
import { Form, Input, Button, Select } from 'antd';
import TextArea from 'antd/lib/input/TextArea';
import FormItem from 'antd/lib/form/FormItem';


class CreateLessonForm extends React.Component {

  handleFormSubmit = (event) => {
    event.preventDefault();
    // const subject = event.target.elements.subject.value
    // const title = event.target.elements.title.value
    // const content = event.target.elements.content.value
    console.log(event)
  }

  // state = {
  //   options: []
  // }



  render() {
    return (
      <div>
        <Form onSubmit={this.handleFormSubmit}>
          <FormItem label="Избери предмет">
            <Select name="subject" options={[{value: 'БЕЛ', label: 'Български език и литература'}]}>
            </Select>
          </FormItem>

          <Form.Item label="Заглавие">
            <Input name="title" placeholder="Въведете заглавие на урока" />
          </Form.Item>

          <Form.Item label="Съдържание">
            <TextArea name="content" />
          </Form.Item>
          <FormItem>
            {/* <Button type="primary" htmlType="Submit">Изпрати</Button> */}
            <Input type="submit" value="Изпрати" />
          </FormItem>
        </Form>
      </div>
    );
  };
};


export default CreateLessonForm;