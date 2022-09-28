//SPDX-License-Identifier:UNLICENSED
pragma solidity ^0.8.7;

contract Bank {
    uint256 totalBalanceOfContract = 0;

    function getContractBalance() public view returns (uint256) {
        return totalBalanceOfContract;
    }

    mapping(address => uint256) public balances;
    mapping(address => uint256) depositeTimeStamp;

    function addBalance() public payable {
        balances[msg.sender] = msg.value;
        totalBalanceOfContract = totalBalanceOfContract + msg.value;
        depositeTimeStamp[msg.sender] = block.timestamp;
    }

    function getBalance(address userAddress) public view returns (uint256) {
        uint256 principal = balances[userAddress];
        uint256 timeElapsed = block.timestamp - depositeTimeStamp[userAddress];
        return
            principal +
            uint256(
                (principal * 7 * timeElapsed) / (100 * 365 * 24 * 60 * 60)
            ) +
            1;
    }

    function withdraw(uint256 ammount) public payable {
        address payable withdrawto = payable(msg.sender);
        withdrawto.transfer(ammount);
        totalBalanceOfContract = totalBalanceOfContract - ammount;
        balances[msg.sender] = totalBalanceOfContract;
    }
}
