//SPDX-License-Identifier:UNLICENSED
pragma solidity ^0.8.7;

contract studenData {
    string[] public addSubject;

    struct student {
        string name;
        uint256 mobileNo;
        string emailAddress;
        string[] subjects;
    }

    mapping(uint256 => student) public class;

    function addStudent(
        uint256 _rollno,
        string memory _sname,
        uint256 _number,
        string memory _email,
        string memory _subject1,
        string memory _subject2,
        string memory _subject3
    ) public {
        addSubject.push(_subject1);
        addSubject.push(_subject2);
        addSubject.push(_subject3);
        class[_rollno] = student(_sname, _number, _email, addSubject);
    }

    address payable public schoolAccount =
        payable(0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2);

    function payfees() public payable {
        schoolAccount.transfer(msg.value);
    }
}
