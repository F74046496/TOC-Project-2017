# TOC Project 2017

Template Code for TOC Project 2017

A telegram bot based on a finite state machine

## Finite State Machine
![fsm](./img/show-fsm.png)

## �D�D: �o�v�H��
���Uı�o�L�᪺�o�v�M�w���U�ӭn������ơA��֥L�̦]�������ұ��Ү��O���j�q�ɶ��C

##����:
�ݥ��ϥ�`ngrok`���oURL�A���۰���
```sh
python3 app.py
```
�T�w�إ߳s���Y�i�ϥ�Telegram�PChatBot���

##�p�󤬰�:

The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

###state:

*user

*state1

*state2

*Bored

*Sweated

*Annoyed

*Excited

*Tired

*Sleeping

�b�i�J`Bored`���᳣�|��''���ܥi�H��J���r��A�������~�]���|send�@�i�Ϥ��A�䤤`Excited`���F�򥻹Ϥ��٦����ѭ��ֵ��ϥΪ̲�ť�C

�q`user`��J"feel bored"��|�i�J`Bored`

*user

	*input: "feel bored" go to `Bored`

*Bored

	*input: "sail" go to `Sweated`

	*input: "study" go to `Annoyed`

	*input: "relax" go to `Excited`

*Sweated

	*input: "take a shower" go to `Tired`

*Annoyed

	*input: "study more" go to `Tired`

	*input: "relax" go to `Excited`

*Excited

	*input: "study" go to `Annoyed`

	*input: "relax" stay in `Excited`

*Tired

	*input: "sleep" go to `Sleeping`

*Sleeping

	*just go back `user`



## Author
[F74046496](https://github.com/F74046496)
