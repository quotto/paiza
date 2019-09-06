#! coding:utf-8
#! ruby-1.9.2

#総発表数
N = gets.to_i

speakerArray = Array.new(N)

N.times do |n|
  i = n
  speakerArray[i] = Array.new(2)

  inputLines = gets.split(' ')
  speakerArray[i][0] = inputLines[0]
  speakerArray[i][1] = inputLines[1].to_i
end

hour = 10
min = 0

speakerArray.each do |speakerInfoArray| 
  name = speakerInfoArray[0]
  speakTime = speakerInfoArray[1]

  startHour = endHour = hour
  startMin = min
  endMin = startMin + speakTime
  # 60分を超えた場合は時間を1進める
  if endMin >= 60
    endHour += 1
    endMin -= 60
  end
  if startHour == 12 || endHour == 12
    # 開始時刻が12時もしくは終了後の時刻が12時になった場合、開始・終了時刻を修正
    # 休憩時間10分を巻き戻す
    startMin -= 10
    endMin -= 10
    # 00分より前に戻った場合は時間を1戻す
    if startMin < 0
      startMin += 60
      startHour -= 1
    end
    if endMin < 0
      endMin += 60
      endHour -= 1
    end
    # 開始終了後の時刻を1時間ずらす
    startHour += 1
    endHour += 1
  end
  print "#{startHour}:#{sprintf("%02d",startMin)} - "
  puts "#{endHour}:#{sprintf("%02d",endMin)} #{name}"

  # 休憩時間を考慮し次の開始時間を算出する
  hour = endHour
  min = endMin + 10
  if min >= 60
    hour = endHour + 1
    min = min - 60
  end
end