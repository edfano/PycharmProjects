import paramiko

#Use paramiko library python Establish a SSH connection using:

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.252.164.160',support,cod.wocks)

#Check the status if connection is alive using :
status =  ssh.get_transport().is_active()

'''
returns True if connection is alive/active
ssh.exec_command() is basically a single session. Use exec_command(command1;command2) to execute multiple commands in one session

Also, you can use this to execute multiple commands in single session
'''

channel = ssh.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')
stdin.write('''
  cd /u/easy/ep2
  ls -lrt
  ''')

print(stdout.read())