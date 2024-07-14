import { Card } from 'antd';

function TaskCard() {

    return (
      <>
        <Card
      title="Task"
      extra={<a href="#">More</a>}
      style={{
        width: 300,
      }}
    >
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
      </>
    )
  }
  
  export default TaskCard
  