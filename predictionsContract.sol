pragma solidity ^0.7.0;

contract Predictions {
    
    // Set 2 options
    enum Side { option1, option2 }
    struct Result {
        Side winner;
        Side loser;
    }
    Result public result;
    
    // Verify event is completed before funds are paid out
    bool public eventFinished;
    
    mapping(Side => uint) public bets;
    mapping(address => mapping(Side => uint)) public betsPerGambler;
    address public oracle;
    
    constructor(address _oracle) {
        oracle = _oracle;
    }
    // function to create a bet
    function createBet(Side _side) external payable {
        require(eventFinished == false, 'This event is already finished.');
        bets[_side] += msg.value;
        betsPerGambler[msg.sender][_side] += msg.value;
    }
    
    // function for each player to withdraw after the event
    function payout() external {
        uint gamblerBet = betsPerGambler[msg.sender][result.winner];
        require(gamblerBet > 0, 'You do not have a winning bet');
        require(eventFinished == true, 'This event is not finished yet');
        // payout: pay the player their initial bet + their stake in the loser's bets
        uint gain = gamblerBet + bets[result.loser] * gamblerBet / bets[result.winner];
        // after winnings have been paid, set both sides = 0 to refresh
        betsPerGambler[msg.sender][Side.option1] = 0;
        betsPerGambler[msg.sender][Side.option2] = 0;
        msg.sender.transfer(gain);
    }
    
    function reportResult(Side _winner, Side _loser) external {
        require(oracle == msg.sender, 'Only the Oracle can report the results');
        require(eventFinished == false, 'This event is not finished yet.');
        result.winner = _winner;
        result.loser = _loser;
        eventFinished = true;
    }
}