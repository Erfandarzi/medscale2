set -e

cudaid=$1
sample_num=$2
mu=$3

# mu=(0.1 1.0 5.0)

cd ../../../..

dataset=cora

out_dir=out_${dataset}_prox

echo "HPO starts..."

lrs=(0.01 0.01668 0.02783 0.04642 0.07743 0.12915 0.21544 0.35938 0.59948 1.0)
wds=(0.0 0.001 0.01 0.1)
dps=(0.0 0.5)
steps=(1 2 3 4 5 6 7 8)

for ((l = 0; l < ${#lrs[@]}; l++)); do
  for ((w = 0; w < ${#wds[@]}; w++)); do
    for ((d = 0; d < ${#dps[@]}; d++)); do
      for ((s = 0; s < ${#steps[@]}; s++)); do
        for k in {1..3}; do
<<<<<<< HEAD
          python medscale/main.py --cfg benchmark/FedHPOBench/scripts/gcn/cora_prox.yaml device $cudaid train.optimizer.lr ${lrs[$l]} fedprox.use True fedprox.mu ${mu} train.optimizer.weight_decay ${wds[$w]} model.dropout ${dps[$d]} train.local_update_steps ${steps[$s]} federate.sample_client_num $sample_num seed $k outdir ${out_dir}/${sample_num} expname lr${lrs[$l]}_wd${wds[$w]}_dropout${dps[$d]}_step${steps[$s]}_mu${mu}_seed${k} >/dev/null 2>&1
=======
<<<<<<< HEAD
          python medscale/main.py --cfg benchmark/FedHPOBench/scripts/gcn/cora_prox.yaml device $cudaid train.optimizer.lr ${lrs[$l]} fedprox.use True fedprox.mu ${mu} train.optimizer.weight_decay ${wds[$w]} model.dropout ${dps[$d]} train.local_update_steps ${steps[$s]} federate.sample_client_num $sample_num seed $k outdir ${out_dir}/${sample_num} expname lr${lrs[$l]}_wd${wds[$w]}_dropout${dps[$d]}_step${steps[$s]}_mu${mu}_seed${k} >/dev/null 2>&1
=======
          python medscale/main.py --cfg benchmark/FedHPOBench/scripts/gcn/cora_prox.yaml device $cudaid train.optimizer.lr ${lrs[$l]} fedprox.use True fedprox.mu ${mu} train.optimizer.weight_decay ${wds[$w]} model.dropout ${dps[$d]} train.local_update_steps ${steps[$s]} federate.sample_client_num $sample_num seed $k outdir ${out_dir}/${sample_num} expname lr${lrs[$l]}_wd${wds[$w]}_dropout${dps[$d]}_step${steps[$s]}_mu${mu}_seed${k} >/dev/null 2>&1
>>>>>>> fe4962455354c9c11afd9c9806ceda28eb280737
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
        done
      done
    done
  done
done

echo "HPO ends."
