import React from 'react';
import { List, Space } from 'antd';
import { StarOutlined } from '@ant-design/icons';
import '../App.css';
// import { Link } from 'react-router-dom';

const IconText = ({ icon, text }) => (
  <Space>
    {React.createElement(icon)}
    {text}
  </Space>
);

const Lesson = (props) => {
    return (
        <List
            itemLayout="vertical"
            size="large"
            pagination={{
            onChange: page => {
            console.log(page);
            },
            pageSize: 3,
            }}
            dataSource={props.data}
            // footer={}
            renderItem={item => (
            <List.Item
                // key={item.title}
                // actions={[
                // <IconText icon={StarOutlined} text="156" key="list-vertical-star-o" />,
                // <IconText icon={LikeOutlined} text="156" key="list-vertical-like-o" />,
                // <IconText icon={MessageOutlined} text="2" key="list-vertical-message" />,
                // ]}
                actions={[
                        <IconText icon={StarOutlined} text={'~'.repeat(100)} key="list-vertical-star-o" />,
                ]}
                extra={
                <img
                    width={272}
                    alt="logo"
                    src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                />
                }>

            <List.Item.Meta
                // avatar={<Avatar src={item.avatar} />}
                title={<a href={`/${item.id}`}>{item.title}</a>}
                description={item.description} />
                <p>{item.content}</p>
            </List.Item>)}  
        />
    );
}

export default Lesson;