//SPDX-License-Identifier:UNLICENSED
pragma solidity ^0.8.7;

contract Ballot {
    //VARIABLE

    struct vote {
        address voterAddress;
        bool choice;
    }

    struct voter {
        string voterName;
        bool voted;
    }

    uint256 private countResult = 0;
    uint256 public finalResult = 0;
    uint256 public totalVoters = 0;
    uint256 public totalVotes = 0;

    mapping(uint256 => vote) private votes;
    mapping(address => voter) public voterRegister;

    address public ballotOfficialAddress;
    string public ballotOfficialName;
    string public proposal;

    enum State {
        Created,
        Voting,
        Ended
    }
    State public state;

    //MODIFIERS
    modifier condition(bool _condition) {
        require(_condition);
        _;
    }

    modifier onlyOfficial() {
        require(msg.sender == ballotOfficialAddress);
        _;
    }

    modifier inState(State _state) {
        require(state == _state);
        _;
    }

    //EVENTS

    //FUNCTIONS

    constructor(string memory _ballotOfficialName, string memory _propasl) {
        ballotOfficialAddress = msg.sender;
        ballotOfficialName = _ballotOfficialName;
        proposal = _propasl;

        state = State.Created;
    }

    function addVoter(address _voterAddress, string memory _voterName)
        public
        inState(State.Created)
        onlyOfficial
    {
        voter memory v;
        v.voterName = _voterName;
        v.voted = false;

        voterRegister[_voterAddress] = v;
        totalVoters++;
    }

    function startVote() public inState(State.Created) onlyOfficial {
        state = State.Voting;
    }

    function doVote(bool _choice)
        public
        inState(State.Voting)
        returns (bool voted)
    {
        bool found = false;

        if (
            bytes(voterRegister[msg.sender].voterName).length != 0 &&
            !voterRegister[msg.sender].voted
        ) {
            voterRegister[msg.sender].voted = true;
            vote memory v;
            v.voterAddress = msg.sender;
            v.choice = _choice;
            if (_choice) {
                countResult++;
            }
            votes[totalVotes] = v;
            totalVotes++;
            found = true;
        }
        return found;
    }

    function endVote() public inState(State.Voting) onlyOfficial {
        state = State.Ended;
        finalResult = countResult;
    }
}
