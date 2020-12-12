defmodule Policy do
  defp check_policy(lb, ub, count) do
    if count >= lb && count <= ub do
        true
      else
        false
    end
  end
end

File.stream!("input.txt")
|> Stream.map(&String.trim_trailing/1)
|> Enum.to_list
|> Enum.map(fn x -> String.split(x, " ") end)
|> Enum.map(fn ([p, l, s]) ->
  [
    String.split(p, "-"),
    String.graphemes(String.slice(l, 0..0)) |> List.flatten,
    String.graphemes(s)
  ] end)
|> Enum.map(&IO.inspect/1)
|> Enum.map(fn [[lb, ub], l, seq] -> [String.to_integer(lb),String.to_integer(ub),Enum.count(seq, fn c -> c == l end)] end)
|> Enum.map(&IO.inspect/1)
|> Enum.map(fn [lb,ub,c] ->
  if c >= lb && c <= ub do
      true
    else
      false
    end end)
#|> Enum.map(&IO.inspect/1)
