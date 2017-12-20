var Buffer = require('safe-buffer').Buffer // use for Node.js <4.5.0
var VM = require('ethereumjs-vm')

// create a new VM instance
var vm = new VM()

var code =
    //'7f4e616d65526567000000000000000000000000000000000000000000000000003055307f4e616d6552656700000000000000000000000000000000000000000000000000557f436f6e666967000000000000000000000000000000000000000000000000000073661005d2720d855f1d9976f88bb10c1a3398c77f5573661005d2720d855f1d9976f88bb10c1a3398c77f7f436f6e6669670000000000000000000000000000000000000000000000000000553360455560df806100c56000396000f3007f726567697374657200000000000000000000000000000000000000000000000060003514156053576020355415603257005b335415603e5760003354555b6020353360006000a233602035556020353355005b60007f756e72656769737465720000000000000000000000000000000000000000000060003514156082575033545b1560995733335460006000a2600033545560003355005b60007f6b696c6c00000000000000000000000000000000000000000000000000000000600035141560cb575060455433145b1560d25733ff5b6000355460005260206000f3'
'6060604052600436106100405763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663ea8796348114610154575b662386f26fc100003410610152577fec29ee18c83562d4f2e0ce62e38829741c2901da844c015385a94d8c9f03d486600260003660116000604051602001526040517f485631372d00000000000000000000000000000000000000000000000000000081526005810184848082843782019150508260ff167f0100000000000000000000000000000000000000000000000000000000000000028152600101935050505060206040518083038160008661646e5a03f1151561010157600080fd5b5050604051805190506040519081526040602082018190526011818301527f596f7572206b657920697320686572652e00000000000000000000000000000060608301526080909101905180910390a15b005b341561015f57600080fd5b61015260005473ffffffffffffffffffffffffffffffffffffffff9081169030163180156108fc0290604051600060405180830381858888f1935050505015156101a857600080fd5b5600a165627a7a7230582020304ba8cb5786445e5c47f840741111591a38057d40ac139568b31f9eaee3c70029'
var input =
    '773472756d'
var money =
    0x3386F26FC10000

vm.on('step', function (data) {
    console.log(data.opcode.name)
})

vm.runCode({
    code: Buffer.from(code, 'hex'),
    gasLimit: Buffer.from('ffffffff', 'hex'),
    data: Buffer.from(input, 'hex'),
    value: money,
}, function (err, results) {
    console.log(results.logs)
    var str = ''
    for (var j = 0; j < results.logs[0][2].length; j++) {
        var i = results.logs[0][2][j].toString(16)
        if (i.length == 1) {
            i = "0" + i
        }
        str += i
    }
    console.log(str)
})
