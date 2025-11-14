import React from "react";
import Header from "../../components/header/header";
import styled from "styled-components";
import LivingProofAPI from "../../repository/api/livingProofAPI";
import Footer from "../../components/footer/footer";


class LivingProof extends React.Component {
  constructor(props) {
    super(props);
    this.state = {livingProofs: []}
  }

  async componentDidMount() {
    const livingProofs = await LivingProofAPI.fetchLivingProofList();
    this.setState({livingProofs})
  }

  render() {
    const {livingProofs} = this.state;
    return (
      <div>
        <Header/>
        <Container>
          <div className="ui container">
            <div className="ui link cards">
              {livingProofs && livingProofs.map(livingProof => {
                return <div className="card" key={livingProof.id}
                            onClick={() => window.location.href = `/living-proof/${livingProof.id}`}>
                  <div className="image">
                    <img src={livingProof.faceImageURL}/>
                  </div>
                  <div className="content">
                    <div className="header">
                      {`${livingProof.name} (${livingProof.age})`}
                    </div>
                    <div className="meta">
                      {livingProof.occupation}
                    </div>
                    <div className="description">
                      {livingProof.motto}
                    </div>
                  </div>
                </div>
              })}
            </div>
          </div>
        </Container>
        <Footer/>
      </div>)
  }
}

const Title = styled.div`
  margin-top: 5vh;
`;
const Row = styled.div`
  margin-top: 5vh;
`;
const Container = styled.div`
  background-color: #FDF5EE;
  padding-top: 5vh;
  padding-bottom: 7vh;
`;

export default LivingProof;
