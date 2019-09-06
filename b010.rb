#encoding:utf-8
#ruby 1.9.2

#パスを出すチームと背番号
input_lines = gets.split(' ')
PASS_TEAM = input_lines[0]
PASS_NUMBER = input_lines[1].to_i

TEAM_A = gets.split(' ').map(&:to_i)
TEAM_B = gets.split(' ').map(&:to_i)

#パスチームと敵チームに分ける
max = 110 
min = 55
pass_team = TEAM_A
other_team = TEAM_B
if PASS_TEAM == 'B'
  max = 55
  min = 0
  pass_team = TEAM_B
  other_team = TEAM_A
end

#値の昇順に敵チームをソート
other_team.sort!

#パスする選手のポジション
passer_pos = pass_team[PASS_NUMBER - 1]

#一人ずつオフサイド判定を行う
count = 0
pass_team.each_with_index do |i,index|
  #敵陣地にいる
  if i >= min and i <= max
    #パスする選手より前にいる
    judge = PASS_TEAM=='A' ? i >= passer_pos : i <= passer_pos
    if judge
      #敵チームの前から2人目の選手よりも前にいる
      judge = PASS_TEAM=='A' ? i >= other_team[9] : i <= other_team[1]
      if judge
        count += 1
        puts index + 1
      end
    end
  end
end

if count == 0
  puts "None"
end