set -e

cd ../../../../

cudaid=$1
root=$2
dataset=fs_contest_data
method=maml
outdir=exp_out/${method}

if [ ! -d ${outdir} ];then
  mkdir -p ${outdir}
fi

echo "HPO starts..."

lrs=(0.01 0.1 0.05 0.005 0.5)
innerlrs=(0.01 0.1 1.)
local_updates=(1 2 5)
ft_steps=(200 300)


for (( i=0; i<${#lrs[@]}; i++ ))
do
    for (( j=0; j<${#local_updates[@]}; j++ ))
    do
        for (( s=0; s<${#ft_steps[@]}; s++ ))
        do
            for (( ii=0; ii<${#innerlrs[@]}; ii++))
            do
                log=${outdir}/gin_lr-${lrs[$i]}_step-${local_updates[$j]}_mstep-${ft_steps[$s]}_ilr-${innerlrs[$ii]}_on_${dataset}.log
                for k in {1..3}
                do
<<<<<<< HEAD
                    python medscale/main.py --cfg benchmark/B-FHTL/scripts/Grpah-DC/fedavg_gnn_minibatch_on_multi_task.yaml \
=======
<<<<<<< HEAD
                    python medscale/main.py --cfg benchmark/B-FHTL/scripts/Grpah-DC/fedavg_gnn_minibatch_on_multi_task.yaml \
=======
                    python federatedscope/main.py --cfg benchmark/B-FHTL/scripts/Grpah-DC/fedavg_gnn_minibatch_on_multi_task.yaml \
>>>>>>> fe4962455354c9c11afd9c9806ceda28eb280737
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
                    data.root ${root} \
                    device ${cudaid} \
                    data.type ${dataset} \
                    optimizer.lr ${lrs[$i]} \
                    federate.local_update_steps ${local_updates[$j]} \
                    trainer.type graphmaml_trainer \
                    trainer.finetune.before_eval True \
                    trainer.finetune.steps ${ft_steps[$s]} \
                    maml.use True \
                    maml.inner_lr ${innerlrs[$ii]} \
                    eval.freq 100 \
                    seed $k >>${log} 2>&1
                done
<<<<<<< HEAD
                python medscale/parse_exp_results.py --input ${log}
=======
<<<<<<< HEAD
                python medscale/parse_exp_results.py --input ${log}
=======
                python federatedscope/parse_exp_results.py --input ${log}
>>>>>>> fe4962455354c9c11afd9c9806ceda28eb280737
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
            done
        done
    done
done

echo "HPO ends."
