import './App.css';
import FinalScoreCard from './FinalScoreCard';
import JobCard from './JobCard';
import ScoreCard from './ScoreCard';
import ChatComponent from './ChatComponent';
function App() {
  const randomDate = "Nov 4, 2023";
  const randomJobName = "Software Developer Manager";
  const randomLocation = "New York, NY";
  const randomNumCandidates = Math.floor(Math.random() * 100); // Generate a random number of candidates
  const conversationData = [
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'user' },
    { text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, esse nulla non ab nobis iure aliquam earum perferendis numquam molestias. Temporibus alias hic est magni. Dolore quibusdam a illum libero?', sender: 'bot' },
    // Add more messages as needed
  ];
  return (
    <div className="App" style={{backgroundColor:'#edf0f2'}}>
      <JobCard
        date={randomDate}
        jobName={randomJobName}
        location={randomLocation}
        numCandidates={randomNumCandidates}
      />

      {/* <ScoreCard title="Leadership Score" score={10} /> */}

      {/* <FinalScoreCard title={'Overall Score'} score={33} />  */}

      {/* <ChatComponent conversation={conversationData} /> */}
     

    </div>
  );
}

export default App;
