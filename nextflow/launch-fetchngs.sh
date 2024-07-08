nextflow run nf-core/fetchngs \
	-profile docker,awsbatch \
	-work-dir s3://genomic-nextflow/fetchngs/work/ \
	--awsqueue genomic-nextflow-queue \
	--awsregion us-east-1 \
	--input s3://genomic-nextflow/sample.csv \
	--outdir s3://genomic-nextflow/fetchngs/output/ \
	--nf_core_pipeline rnaseq \
	--download_method sratools